mod common;

use common::get_start;
use common::parse_grid;
use std::collections::HashSet;
use std::time::Instant;

/// Traverses the grid to determine if a loop occurs.
///
/// # Arguments
///
/// * `grid` - A reference to a 2D vector of characters representing the grid.
/// * `start` - where to start moving from
///
/// # Returns
///
/// * `Result<(bool, Vec<(i32, i32)>), String>` - A tuple where:
///     * `bool` indicates if the guard exited the grid.
///     * `Vec<(i32, i32)>` contains the visited locations.
///     * `String` contains an error message if an error occurs.
fn traverse_grid(
    grid: &Vec<Vec<char>>,
    start: &(i32, i32),
) -> Result<(bool, HashSet<(i32, i32)>), String> {
    let directions: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    let mut dir_index = 0;
    let mut visited: HashSet<(i32, i32, i32, i32)> = HashSet::new();

    let (mut cx, mut cy) = start.clone();
    let (dx, dy) = get_direction(directions, dir_index)?;
    visited.insert((cx, cy, dx, dy));

    loop {
        let (dx, dy) = get_direction(directions, dir_index)?;
        let (nx, ny) = (cx + dx, cy + dy);

        if out_of_bounds(grid, nx, ny) {
            let locs: HashSet<(i32, i32)> = visited.iter()
                .map(|(x, y, dx, dy)| (*x, *y))
                // .filter(|coord| coord != start)
                .collect();

            return Ok((true, locs));
        }

        let cell: &char = get_cell_value(grid, nx, ny)?;

        if *cell == '#' {
            dir_index += 1;
            dir_index %= directions.len();
            continue;
        }

        if *cell == '.' {
            let key: (i32, i32, i32, i32) = (nx, ny, dx, dy);
            if visited.contains(&key) {
                return Ok((false, HashSet::new()));
            }
            visited.insert(key);

            (cx, cy) = (nx, ny);
            continue;
        }
    }
}

fn get_direction(directions: [(i32, i32); 4], dir_index: usize) -> Result<(i32, i32), String> {
    directions
        .get(dir_index)
        .cloned()
        .ok_or_else(|| "failed to get dir".to_string())
}

fn set_cell_value(grid: &mut Vec<Vec<char>>, row: i32, col: i32, val: char) -> Result<(), String> {
    let cell = grid
        .get_mut(row as usize)
        .and_then(|item| item.get_mut(col as usize))
        .ok_or_else(|| "Failed to get cell")?;

    *cell = val;

    Ok(())
}

fn get_cell_value(grid: &Vec<Vec<char>>, nx: i32, ny: i32) -> Result<&char, String> {
    grid.get(nx as usize)
        .and_then(|item| item.get(ny as usize))
        .ok_or_else(|| "No such cell".to_string())
}

fn out_of_bounds(grid: &Vec<Vec<char>>, nx: i32, ny: i32) -> bool {
    !(0 <= nx && nx < grid.len() as i32 && 0 <= ny && ny < grid[0].len() as i32)
}

pub fn main() -> Result<(), String> {
    let content = include_str!("input.txt");
    let timer = Instant::now();

    let mut grid: Vec<Vec<char>> = parse_grid(content);

    // Find the starting position ('^') in the grid
    let start: (i32, i32) = get_start(&grid)?; // Convert None to an error
    let (i, j) = start;
    grid[i as usize][j as usize] = '.'; // Replace the start with a '.'

    let (_, path) = traverse_grid(&grid, &start)?;

    let mut obstacles = 0;
    for (row, col) in path {
        set_cell_value(&mut grid, row, col, '#')?;

        let (exited, _) = traverse_grid(&grid, &start)?;
        if !exited && (row, col) != start {
            obstacles += 1;
        }

        set_cell_value(&mut grid, row, col, '.')?;
    }

    let duration = timer.elapsed();
    println!("Part 2: {}", obstacles); // 1703
    println!("Time: {:.2?}", duration);

    Ok(())
}
