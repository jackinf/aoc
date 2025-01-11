use std::collections::HashSet;

mod common;

use crate::common::parse_grid;
use common::get_start;

fn traverse_grid(grid: &[Vec<char>], i: i32, j: i32) -> Result<usize, String> {
    let directions: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    let mut dir_index = 0;

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut cx = i;
    let mut cy = j;
    loop {
        visited.insert((cx, cy));
        let (dx, dy) = directions
            .get(dir_index)
            .ok_or_else(|| "failed to get dir".to_string())?;
        let (nx, ny) = (cx + dx, cy + dy);

        if !(0 <= nx && nx < grid.len() as i32 && 0 <= ny && ny < grid[0].len() as i32) {
            return Ok(visited.len());
        }

        let cell: &char = grid
            .get(nx as usize)
            .and_then(|item| item.get(ny as usize))
            .ok_or_else(|| "No such cell".to_string())?;

        if *cell == '#' {
            dir_index += 1;
            dir_index %= directions.len();
            continue;
        }

        if *cell == '.' {
            (cx, cy) = (nx, ny);
            continue;
        }

        return Err("Invalid cell type".to_string());
    }
}

pub fn main() -> Result<(), String> {
    let content = include_str!("input.txt");

    let mut grid: Vec<Vec<char>> = parse_grid(content);

    // Find the starting position ('^') in the grid
    let start: (i32, i32) = get_start(&grid)?; // Convert None to an error
    let (i, j) = start;
    grid[i as usize][j as usize] = '.'; // Replace the start with a '.'

    let result = traverse_grid(&mut grid, i, j)?;

    println!("Part 1: {}", result);

    Ok(())
}
