use std::cmp;
use std::cmp::min;
use std::collections::{HashMap, HashSet};
use log::debug;
use env_logger;

fn debug_grid(grid: &[Vec<char>]) {
    for row in grid {
        debug!("{:?}", row);
    }
}

pub fn main() {
    env_logger::init();
    // env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();

    let content = include_str!("sample1.txt");

    let mut grid: Vec<Vec<char>> = content.lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    let width = grid.first().unwrap().len();
    let height = grid.len();

    debug_grid(&grid);

    // find coordinates
    let mut type_coords: HashMap<char, HashSet<(i32, i32)>> = HashMap::new();
    for (row_i, row) in grid.iter().enumerate() {
        for (col_i, val) in row.iter().enumerate() {
            // let (x, y) = (row_i.min(col_i), row_i.max(col_i));
            let x = cmp::min(row_i, col_i) as i32;
            let y = cmp::max(row_i, col_i) as i32;

            type_coords.entry(*val).or_insert_with(HashSet::new).insert((x, y));
        }
    }
    type_coords.remove(&'.');

    println!("Type coords");
    debug!("{:?}", type_coords);

    // find pairs
    let mut pairs: HashMap<char, Vec<((i32, i32), (i32, i32))>> = HashMap::new();
    for (symbol, coords) in type_coords.iter() {
        let coords: Vec<(i32, i32)> = coords.iter().cloned().collect();
        for i in 0..coords.len() - 1 {
            let coord1 = coords[i];
            for j in i+1..coords.len() {
                let coord2 = coords[j];
                pairs.entry(*symbol).or_insert_with(Vec::new).push((coord1, coord2));
            }
        }
    }

    println!("Pairs");
    debug!("{:?}", pairs);

    // calculate distances between each pair
    let mut results: HashSet<(char, i32, i32)> = HashSet::new();
    for (symbol, symbol_pairs) in pairs.iter() {
        for ((x1, y1), (x2, y2)) in symbol_pairs.iter() {
            let (xd, yd) = (x1 - x2, y1 - y2);
            let (nx1, ny1) = (x1 + xd, y1 + yd);
            let (nx2, ny2) = (x2 + xd, y2 + yd);
            results.insert((*symbol, nx1, ny1));
            results.insert((*symbol, nx2, ny2));
        }
    }

    println!("Results");
    debug!("{:?}", results);

    // remove out of bounds
    let mut results2: HashSet<(char, i32, i32)> = HashSet::new();
    for (symbol, x, y) in results.iter() {
        if 0 <= *x && *x < height as i32 && 0 <= *y && *y < width as i32 {
            results2.insert((*symbol, *x, *y));
            grid[*x as usize][*y as usize] = '#';
        }
    }

    println!("Results2");
    debug!("{:?}", results2);

    let final_result = results2.len();
    println!("Part 1: {}", final_result);
}