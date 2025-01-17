use std::{env, fs};
use std::collections::HashSet;
use anyhow::{Result, anyhow};

type Coord = (i32, i32);

fn parse_coordinates(line: &str) -> Result<Coord> {
    let coords = line.split(':')
        .nth(1)
        .ok_or(anyhow!("Missing colon in line {}", line))?
        .split(',')
        .map(|part| {
            part.trim()
                .chars()
                .skip(2) // Skip "X+", "Y+", etc.
                .collect::<String>()
                .parse::<i32>()
                .map_err(|e| anyhow!("Failed to parse coordinate {}", e))
        }).collect::<Result<Vec<_>>>()?;

    let [x, y]: [i32; 2] = coords.try_into().map_err(|_| anyhow!("Invalid coordinate format"))?;
    Ok((x, y))
}

fn find_coordinates(a: i32, b: i32, pr: i32, a_cost: i32, b_cost: i32) -> Result<HashSet<Coord>> {
    if a < b {
        return find_coordinates(b, a, pr, b_cost, a_cost);
    }

    let max_a_button_presses = pr / a;
    let mut candidates: HashSet<Coord> = Default::default();

    for a_presses in (0..max_a_button_presses).rev() {
        if a_presses > 100 {
            continue
        }

        let remainder_steps = pr - a;

        if remainder_steps % b == 0 {
            let b_presses = remainder_steps / b;
            if b > 100 {
                continue
            }

            if a_cost == 3 && b_cost == 1 {
                candidates.insert((a_presses, b_presses));
            } else {
                candidates.insert((b_presses, a_presses));
            }
        }
    }

    Ok(candidates)
}

fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();

    let file_path = format!("{}/bin/2024/day13/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path)?;
    // let normalized_content = content.replace("\r\n", "\n");
    // let blocks: Vec<&str> = normalized_content.split("\n\n").collect();

    let blocks: Vec<_> = content.lines()
        .collect::<Vec<_>>()
        .split(|line| line.trim().is_empty())
        .map(|group| group.join("\n"))
        .collect();

    let mut final_result = 0;
    for (_, block_raw) in blocks.iter().enumerate() {
        let lines: Vec<_> = block_raw.lines().collect();

        let (ax, ay) = parse_coordinates(lines.get(0).ok_or(anyhow!("err"))?)?;
        let (bx, by) = parse_coordinates(lines.get(1).ok_or(anyhow!("err"))?)?;
        let (prx, pry) = parse_coordinates(lines.get(2).ok_or(anyhow!("err"))?)?;

        let a_candidates = find_coordinates(ax, bx, prx, 3, 1)?;
        let b_candidates = find_coordinates(ay, by, pry, 3, 1)?;

        let mut common: HashSet<Coord> = Default::default();
        common.extend(a_candidates);
        common.extend(b_candidates);

        if common.len() > 0 {
            let (a_presses, b_presses) = common.iter().next().ok_or(anyhow!("sadf"))?;
            let result = a_presses * 3 + b_presses * 1;
            final_result += result;
        }
    }

    println!("{:?}", final_result);

    Ok(())
}