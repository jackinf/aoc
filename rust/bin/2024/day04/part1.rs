use std::error::Error;

pub fn main() -> Result<(), Box<dyn Error>> {
    let grid: Vec<Vec<char>> = include_str!("input.txt")
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    let rows_count = grid.len();
    let cols_count = grid[0].len();

    // Define the directions: (row_delta, col_delta)
    let directions = [
        (-1, 0),  // Up
        (1, 0),   // Down
        (0, -1),  // Left
        (0, 1),   // Right
        (-1, -1), // Up-Left
        (-1, 1),  // Up-Right
        (1, -1),  // Down-Left
        (1, 1),   // Down-Right
    ];

    // Helper function to get the character at a specific position
    let get_at = |row: isize, col: isize| -> Option<char> {
        if row >= 0 && row < rows_count as isize && col >= 0 && col < cols_count as isize {
            Some(grid[row as usize][col as usize])
        } else {
            None
        }
    };

    let mut found_positions = vec![];

    for row in 0..rows_count {
        for col in 0..cols_count {
            // Check if the current cell is 'X'
            if get_at(row as isize, col as isize) == Some('X') {
                // Check all directions
                for &(drow, dcol) in &directions {
                    let mut is_xmas = true;

                    // Check the next characters in the direction
                    let word = ['M', 'A', 'S'];
                    for (step, &ch) in word.iter().enumerate() {
                        let nrow = row as isize + (step as isize + 1) * drow;
                        let ncol = col as isize + (step as isize + 1) * dcol;

                        if get_at(nrow, ncol) != Some(ch) {
                            is_xmas = false;
                            break;
                        }
                    }

                    if is_xmas {
                        found_positions.push((row, col));
                        // println!("Found 'XMAS' starting at ({}, {}) in direction ({}, {})", row, col, drow, dcol);
                    }
                }
            }
        }
    }

    println!("Part 1: {}", found_positions.len());

    Ok(())
}
