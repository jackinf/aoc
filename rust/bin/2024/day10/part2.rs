use log::debug;
use std::collections::{VecDeque};

type Grid = Vec<Vec<i32>>;

fn parse_grid(content: String) -> Grid {
    content
        .lines()
        .map(|line| {
            line.chars()
                .filter_map(|symbol| symbol.to_digit(10))
                .map(|digit| digit as i32)
                .collect()
        })
        .collect()
}

fn find_starts(grid: &Grid) -> Vec<(i32, i32)> {
    let mut starts = Vec::new();

    for (i, row) in grid.iter().enumerate() {
        for (j, &val) in row.iter().enumerate() {
            if val == 0 {
                starts.push((i as i32, j as i32));
            }
        }
    }

    starts
}

fn out_of_bounds(grid: &Grid, row: i32, col: i32) -> bool {
    row < 0 || col < 0 || row as usize >= grid.len() || col as usize >= grid[row as usize].len()
}

fn traverse(grid: &Grid, start: (i32, i32)) -> Result<i32, String> {
    let mut result: i32 = 0;
    let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    let (start_row, start_col) = start;
    let mut queue: VecDeque<(i32, i32, i32)> = VecDeque::default();

    for (dx, dy) in directions {
        queue.push_back((start_row + dx, start_col + dy, 0));
    }

    while !queue.is_empty() {
        let (row, col, prev_value) = queue.pop_front().ok_or_else(|| "err".to_string())?;

        if out_of_bounds(grid, row, col) {
            continue;
        }

        let curr_value = grid[row as usize][col as usize];
        if curr_value != prev_value + 1 {
            continue;
        }

        if curr_value == 9 {
            result += 1;
            continue;
        }

        for (dx, dy) in directions {
            queue.push_back((row + dx, col + dy, curr_value));
        }
    }

    Ok(result)
}

pub fn main() -> Result<(), String> {
    // env_logger::init();
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();

    let content = include_str!("./input.txt");
    let grid = parse_grid(content.to_string());
    let starts = find_starts(&grid);

    println!("Starts");
    debug!("{:?}", starts);

    let mut final_result = 0;
    for start in &starts {
        let result = traverse(&grid, *start)?;
        final_result += result;
        println!("Result: {}", result);
    }

    debug!("{:?}", grid);

    println!("Part 2: {}", final_result);

    Ok(())
}
