// #![allow(unused)]

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
use crate::prelude::*;
use log::debug;
use std::fs;
use std::fs::read_dir;

mod error;
mod prelude;
mod utils;

const WIDTH: i32 = 71;
const HEIGHT: i32 = 71;
const LIMIT: i32 = 1024;
const STEP_COST: i32 = 1;

const WALL: char = '#';
const EMTPY: char = '.';

fn heuristic(row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
    (row1 - row2).abs() + (col1 - col2).abs()
}

fn a_star(coords: &Vec<(i32, i32)>) -> Result<i32> {
    let mut coords_set: HashSet<(i32, i32)> = HashSet::new();

    for i in 0..coords.len().min(LIMIT as usize) {
        let val: (i32, i32) = coords[i];
        coords_set.insert(val);
    }

    let mut queue = BinaryHeap::new();
    queue.push(Reverse((-1, 0, 0, 1)));
    let mut seen: HashSet<(i32, i32)> = HashSet::new();
    let mut costs: HashMap<(i32, i32), i32> = HashMap::new();
    costs.insert((0, 0), 0);

    while !queue.is_empty() {
        let (_, row, col, steps) = queue.pop().ok_or(Error::Generic("cannot pop".to_string()))?.0;

        if 0 > row || 0 > col || row >= HEIGHT || col >= WIDTH {
            continue;
        }

        if coords_set.contains(&(row, col)) {
            continue;
        }

        // did we make it to the finish
        if row == HEIGHT - 1 && col == WIDTH - 1 {
            return Ok(steps - 1);
        }

        if seen.contains(&(row, col)) {
            continue;
        }
        seen.insert((row, col));

        for (drow, dcol) in [(0, -1), (0, 1), (1, 0), (-1, 0)].iter().rev() {
            let (nrow, ncol) = (row + drow, col + dcol);

            let new_cost = costs.get(&(row, col)).copied().unwrap_or(i16::MAX as i32) + STEP_COST;
            let next_cost = costs.get(&(nrow, ncol)).copied().unwrap_or(i16::MAX as i32) + STEP_COST;

            if new_cost < next_cost {
                costs.insert((nrow, ncol), new_cost);
                let h = heuristic(nrow, ncol, HEIGHT - 1, WIDTH - 1);
                queue.push(Reverse((new_cost + h, nrow, ncol, steps + 1)));
            }
        }
    }

    Err(Error::Generic("Not found".to_string()))
}

pub fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day18/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path)?;

    // parse input
    let mut coords: Vec<(i32, i32)> = vec![];
    for line in content.lines() {
        let mut split = line.split(',');

        let left = split
            .next()
            .and_then(|val| val.parse::<i32>().ok())
            .ok_or(Error::Generic("fail".to_string()))?;
        let right = split
            .next()
            .and_then(|val| val.parse::<i32>().ok())
            .ok_or(Error::Generic("fail".to_string()))?;

        coords.push((left, right));
    }

    // construct grid
    let grid = (0..WIDTH)
        .map(|i| (0..HEIGHT).map(|_| '.').collect::<Vec<char>>())
        .collect::<Vec<_>>();

    // a star
    let steps = a_star(&coords)?;

    // wrong answer: curr 230 vs real 360
    println!("Part 1: {}", steps);

    Ok(())
}
