use std::collections::HashSet;

use log::info;

type Grid = Vec<Vec<char>>;

fn main() {
    env_logger::init();

    let contents = include_str!("sample0.txt");
    let grid: Grid = contents.lines()
        .map(|line| line.chars().collect())
        .collect();

    let (start_row, start_col) = find_start(&grid).unwrap_or_default();

    let mut hit_splitters: HashSet<(usize, usize)> = HashSet::new();
    solve(&grid, (start_row, start_col), &mut hit_splitters);

    let total_score = hit_splitters.len();
    info!("{total_score}");
}

fn find_start(grid: &Grid) -> Option<(usize, usize)> {
    for row in 0..grid.len() {
        for col in 0..grid[0].len() {
            if grid[row][col] == 'S' {
                return Some((row, col));
            }
        }
    }

    None
}

fn solve(grid: &Grid, curr: (usize, usize), hit_splitters: &mut HashSet<(usize, usize)>) {
    let (row, col) = curr;

    // Made it to the bottom
    if row >= grid.len() {
        return;
    }

    // Cache
    if hit_splitters.contains(&(row, col)) {
        return;
    }
    
    // Found a splitter
    if grid[row][col] == '^' {
        // Record a score from a splitter
        hit_splitters.insert((row, col));

        if col > 0 { 
            solve(&grid, (row + 1, col - 1), hit_splitters);
        };
        
        if col < grid[row].len() - 1 { 
            solve(&grid, (row + 1, col + 1), hit_splitters);
        };
    } else {
        // Continue going down
        solve(&grid, (row + 1, col), hit_splitters);
    }
}