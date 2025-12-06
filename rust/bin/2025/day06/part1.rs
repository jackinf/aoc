use std::collections::VecDeque;

use log::{debug, info};

fn main() {
    env_logger::init();

    let contents = include_str!("input.txt");
    let mut lines: VecDeque<Vec<&str>> = contents.split("\n")
        .map(|line| line.trim().split_whitespace().collect())
        .collect();
    debug!("LINES = {:?}", lines);

    let operations = VecDeque::from(lines.pop_back().unwrap());
    debug!("OPERATIONS = {:?}", operations);

    let problems = transpose(lines);
    debug!("PROBLEMS = {:?}", problems);

    assert_eq!(problems.len(), operations.len());

    let mut result = 0u128;

    for i in 0..problems.len() {
        let op = operations[i];
        let problem = problems.get(i).unwrap();
        if op == "+" {
            let sub_res: u128 = problem.iter().sum();
            result += sub_res;
        } else if op == "*" {
            let sub_res: u128 = problem.iter().product();
            result += sub_res;
        }
    }

    info!("{result}");
}

fn transpose(grid: VecDeque<Vec<&str>>) -> Vec<Vec<u128>> {
    let rows = grid.len();
    let cols = grid[0].len();

    (0..cols)
        .map(|col| {
            (0..rows)
                .map(|row| grid[row][col].parse::<u128>().unwrap())
                .collect()
        })
        .collect()
}