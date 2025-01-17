use std::collections::HashSet;
use std::fs;
use std::io;

type Grid = Vec<Vec<char>>;

fn read_grid(file_path: String) -> Result<Grid, io::Error> {
    let content = fs::read_to_string(file_path)?;

    Ok(content
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<_>>())
}

fn get(grid: &Grid, row: i32, col: i32) -> Option<char> {
    if 0 > row || 0 > col || row >= grid.len() as i32 || col >= grid[0].len() as i32 {
        return None;
    }

    Some(grid[row as usize][col as usize])
}

fn count_corners(grid: &Grid, row: i32, col: i32) -> i32 {
    let mut total_corner_count = 0;

    /*
       n00 n01 n02
       n10 n11 n12
       n20 n21 n22
    */

    let n00 = get(grid, row - 1, col - 1);
    let n01 = get(grid, row - 1, col);
    let n02 = get(grid, row - 1, col + 1);

    let n10 = get(grid, row, col - 1);
    let n11 = get(grid, row, col);
    let n12 = get(grid, row, col + 1);

    let n20 = get(grid, row + 1, col - 1);
    let n21 = get(grid, row + 1, col);
    let n22 = get(grid, row + 1, col + 1);

    // open corners - two neighbors are same, and diagonally is different
    if n11 == n10 && n11 == n01 && n11 != n00 {
        total_corner_count += 1
    }
    if n11 == n12 && n11 == n01 && n11 != n02 {
        total_corner_count += 1
    }
    if n11 == n10 && n11 == n21 && n11 != n20 {
        total_corner_count += 1
    }
    if n11 == n12 && n11 == n21 && n11 != n22 {
        total_corner_count += 1
    }

    // closed corners
    if n11 != n10 && n11 != n01 {
        total_corner_count += 1
    }
    if n11 != n12 && n11 != n01 {
        total_corner_count += 1
    }
    if n11 != n10 && n11 != n21 {
        total_corner_count += 1
    }
    if n11 != n12 && n11 != n21 {
        total_corner_count += 1
    }

    total_corner_count
}

fn solve(
    grid: &Grid,
    row: i32,
    col: i32,
    symbol: char,
    seen: &mut HashSet<(i32, i32)>,
) -> Option<(i32, i32)> {
    get(grid, row, col)?;

    if seen.contains(&(row, col)) || grid[row as usize][col as usize] != symbol {
        return None;
    }
    seen.insert((row, col));

    let mut total_areas = 1;
    let mut total_corners = count_corners(grid, row, col);

    let directions: [(i32, i32); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];

    for (dr, dc) in directions {
        if let Some((areas, corners)) = solve(grid, row + dr, col + dc, symbol, seen) {
            total_areas += areas;
            total_corners += corners;
        }
    }

    Some((total_areas, total_corners))
}

pub fn main() -> Result<(), String> {
    let file_path = format!("{}/bin/2024/day12/input.txt", env!("CARGO_MANIFEST_DIR"));
    let grid = read_grid(file_path).map_err(|err| err.to_string())?;

    let mut final_result = 0;
    let mut seen: HashSet<(i32, i32)> = Default::default();

    let height = grid.len();
    let width = grid[0].len();

    for row in 0..height {
        for col in 0..width {
            let symbol = grid[row][col];
            if symbol != '.' {
                if let Some((areas_count, corners_count)) =
                    solve(&grid, row as i32, col as i32, symbol, &mut seen)
                {
                    final_result += areas_count * corners_count;
                }
            }
        }
    }

    println!("Part 2: {}", final_result); // 818286

    Ok(())
}
