use anyhow::{anyhow, Result};
use log::debug;
use std::fs;
use std::mem::swap;

type Robot = (i64, i64, i64, i64);
type Robots = Vec<Robot>;
// type Q4Safety = (i64, i64, i64, i64);

#[derive(Debug, Default)]
struct Q4Safety {
    p0: i64,
    p1: i64,
    p2: i64,
    p3: i64,
}

impl Q4Safety {
    fn total(&self) -> i64 {
        self.p0 * self.p1 * self.p2 * self.p3
    }
}

const WIDTH: i64 = 101;
const HEIGHT: i64 = 103;
const MAX_SECONDS: i64 = 100;

fn parse_part(left: &str) -> Result<(i64, i64)> {
    let coordinates: Vec<i64> = left
        .chars()
        .skip(2)
        .collect::<String>()
        .split(',')
        .map(|val| val.parse::<i64>().map_err(|_| anyhow!("failed to parse")))
        .collect::<Result<Vec<_>, _>>()?;

    let [col, row]: [i64; 2] = coordinates.try_into().map_err(|_| anyhow!("Expected exactly 2 coordinates"))?;

    Ok((col, row))
}

fn parse_robots(content: String) -> Result<Vec<Robot>> {
    let mut robots = vec![];

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();

        let [left, right]: [&str; 2] = parts.try_into().map_err(|_| anyhow!("Invalid line format: {}", line))?;

        let (col, row) = parse_part(left)?;
        let (col_delta, row_delta) = parse_part(right)?;

        let robot: Robot = (col, row, col_delta, row_delta);
        robots.push(robot);
    }

    Ok(robots)
}

fn step(state1: &Robots) -> Robots {
    let mut state2: Robots = Vec::new();

    for (col, row, col_delta, row_delta) in state1.into_iter() {
        let col2 = (col + col_delta) % WIDTH;
        let row2 = (row + row_delta) % HEIGHT;
        state2.push((col2, row2, col_delta.clone(), row_delta.clone()))
    }

    state2
}

fn calculate_safety_factor(state: &Robots) -> Q4Safety {
    let mut qs = Q4Safety::default();
    let (w2, h2) = (WIDTH / 2, HEIGHT / 2);

    for (col, row, _, _) in state {
        if *col < w2 && *row < h2 {
            qs.p0 += 1;
        }
        if *col > w2 && *row < h2 {
            qs.p1 += 1;
        }
        if *col < w2 && *row > h2 {
            qs.p2 += 1;
        }
        if *col > w2 && *row > h2 {
            qs.p3 += 1;
        }
    }

    qs
}

pub fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day14/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path).map_err(|_| anyhow!("fail to read contents"))?;
    let mut robots = parse_robots(content).map_err(|_| anyhow!("fail to parse robots"))?;

    debug!("{:?}", robots);

    for _ in 0..MAX_SECONDS {
        let mut robots_next = step(&robots);
        swap(&mut robots, &mut robots_next);
    }

    let qs = calculate_safety_factor(&robots);
    let final_result = qs.total();

    // wrong answer
    println!("Part 1: {}", final_result); // current: 67978958 (correct: 219150360)

    Ok(())
}

/*
[(0, 4, 3, -3),
 (6, 3, -1, -3),
 (10, 3, -1, 2),
 (2, 0, 2, -1),
 (0, 0, 1, 3),
 (3, 0, -2, -2),
 (7, 6, -1, -3),
 (3, 0, -1, -2),
 (9, 3, 2, 3),
 (7, 3, -1, 2),
 (2, 4, 2, -3),
 (9, 5, -3, -3)]
*/