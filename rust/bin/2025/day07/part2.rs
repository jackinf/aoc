use std::collections::HashSet;

use log::info;

type Grid = Vec<Vec<char>>;

fn main() {
    env_logger::init();

    let contents = include_str!("input.txt");
    let grid: Grid = contents.lines()
        .map(|line| line.chars().collect())
        .collect();

    let (start_row, start_col) = find_start(&grid).unwrap_or_default();

    let mut seen: HashSet<(usize, usize)> = HashSet::new();
    let total_score = 1 + solve(&grid, (start_row, start_col), &mut seen);

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

fn solve(grid: &Grid, curr: (usize, usize), seen: &mut HashSet<(usize, usize)>) -> u32 {
    let (row, col) = curr;

    // Made it to the bottom
    if row >= grid.len() {
        return 0;
    }
    
    // Found a splitter
    if grid[row][col] == '^' {
        // Check if this splitter has already been hit
        // if seen.contains(&(row, col)) {
        //     return 0;
        // }
        // seen.insert((row, col));

        // Record a score from a splitter
        let splitter_score = 1;

        let left_score = if col > 0 { solve(&grid, (row + 1, col - 1), seen) } else { 0 };
        let right_score = if col < grid[row].len() - 1 { solve(&grid, (row + 1, col + 1), seen) } else { 0 };
        
        return splitter_score + left_score + right_score;
    }

    // Continue going down
    return solve(&grid, (row + 1, col), seen);
}