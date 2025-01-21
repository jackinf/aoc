use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
use std::error::Error;
use std::fs;
use log::debug;

type Grid = Vec<Vec<char>>;

const STEP_COST: i32 = 1;
const TURN_COST: i32 = 1000;
const DIRECTIONS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
const WALL: char = '#';

fn get_symbl(grid: &Grid, symbol: char) -> Option<(i32, i32)> {
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == symbol {
                return Some((i as i32, j as i32));
            }
        }
    }

    None
}

fn heuristic(row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
    (row1 - row2).abs() + (col1 - col2).abs()
}

fn traverse_grid(grid: &Grid) -> Result<i32, String> {
    let (start_row, start_col) = get_symbl(&grid, 'S').ok_or("fail 1")?;
    let (end_row, end_col) = get_symbl(&grid, 'E').ok_or("fail 2")?;

    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0, 0, start_row, start_col)));
    // let mut queue: VecDeque<(i32, i32, i32, i32)> = VecDeque::from(
    //     [(0, 0, start_row, start_col)]
    // );
    let mut seen: HashSet<(i32, i32)> = HashSet::new();
    let mut costs: HashMap<(i32, i32), i32> = HashMap::from([((start_row, start_col), 0)]);

    while queue.len() > 0 {
        let (_, dir_index, row, col) = queue.pop().ok_or("empty")?.0;

        let cache_key = (row, col);
        if seen.contains(&cache_key) {
            continue;
        }
        seen.insert(cache_key);

        if row == end_row && col == end_col {
            let result = costs.get(&(row, col)).ok_or("no such value")?;
            return Ok(*result);
        }

        for (delta, turn_cost) in [(0, 0), (-1, TURN_COST), (1, TURN_COST)] {
            let new_dir_index = (dir_index + delta) % DIRECTIONS.len() as i32;
            let (row_delta, col_delta) = DIRECTIONS[new_dir_index as usize];
            let (next_row, next_col) = (row + row_delta, col + col_delta);

            let cond1 = 0 <= next_row && next_col < grid.len() as i32;
            let cond2 = 0 <= next_col && next_col < grid[0].len() as i32;
            let cond3 = grid[next_row as usize][next_col as usize] != WALL;

            if cond1 && cond2 && cond3 {
                costs.entry((row, col)).or_insert(9999999);
                let cost: i32 = (*costs.get(&(row, col)).ok_or("fail 3")?).into();

                costs.entry((next_row, next_col)).or_insert(9999999);
                let next_cost = costs.get(&(next_row, next_col)).ok_or("fail")?;

                let new_cost = cost + STEP_COST + turn_cost;

                if new_cost < *next_cost {
                    costs.entry((next_row, next_col)).or_insert(new_cost);
                    let h = heuristic(next_row, next_col, end_row, end_col);
                    queue.push(Reverse((new_cost + h, new_dir_index, next_row, next_col)));
                }
            }
        }
    }

    Err("failed".to_string())
}

pub fn main() -> Result<(), Box<dyn Error>> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day16/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content: String = fs::read_to_string(file_path)?;

    let grid: Grid = content.lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    // debug!("{:?}", grid);

    let final_result = traverse_grid(&grid)?;

    println!("Part 1: {}", final_result);

    Ok(())
}