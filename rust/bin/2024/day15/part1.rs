use log::debug;
use std::{fs, io};
use std::fmt::{Display, Formatter};
use std::mem::swap;
use thiserror;
use thiserror::Error;

type Grid = Vec<Vec<char>>;

#[derive(Error, Debug)]
enum AppError {
    #[error("failed to read file")]
    FailedToReadFile(#[from] io::Error),

    #[error("failed to parse grid")]
    FailedToParseGrid(#[from] ParseGridError),

    #[error("failed to parse movement")]
    FailedToParseMovement(#[from] MovementToDirError),
}

#[derive(Error, Debug)]
enum ParseGridError {
    #[error("Block 1 failed")]
    Block1,

    #[error("Block 2 failed")]
    Block2,
}

fn parse_grid(content: String) -> Result<(Grid, (i32, i32), Vec<char>), ParseGridError> {
    // let content2 = content.replace("\r\n", "\n");
    // let mut blocks = content2.split("\n\n");

    let blocks: Vec<_> = content.lines()
        .collect::<Vec<_>>()
        .split(|line| line.trim().is_empty())
        .map(|group| group.join("\n"))
        .collect();

    let [block1, block2]: [String; 2] = blocks.try_into().map_err(|_| ParseGridError::Block1)?;
    // let block2 = blocks.next().ok_or(ParseGridError::Block2)?;

    let movements: Vec<_> = block2.chars().filter(|char| *char != '\n').collect();

    // debug!("BLOCK 1 = {:?}", block1);
    // debug!("BLOCK 2 = {:?}", movements);

    let mut grid: Grid = Vec::new();
    let mut start: (i32, i32) = (0, 0);

    for (row_i, row) in block1.lines().enumerate() {
        let mut line = Vec::new();
        for (col_i, val) in row.chars().enumerate() {
            if val == '@' {
                start = (row_i as i32, col_i as i32);
                line.push('.')
            } else {
                line.push(val)
            }
        }
        grid.push(line)
    }

    Ok((grid, start, movements))
}

#[derive(Error, Debug)]
enum MovementToDirError {
    #[error("failed to parse movement")]
    FailedToParseMovement
}

fn movement_to_dir(symbol: char) -> Result<(i32, i32), MovementToDirError> {
    match symbol {
        'U' => Ok((-1, 0)),
        'D' => Ok((1, 0)),
        'L' => Ok((0, -1)),
        'R' => Ok((0, 1)),
        _ => Err(MovementToDirError::FailedToParseMovement),
    }
}

#[derive(Error, Debug)]
enum GetGridValueError {
    #[error("Out of bounds")]
    OutOfBounds,
}

fn get_grid_value(grid: &Grid, row: i32, col: i32) -> Result<char, GetGridValueError> {
    // First, ensure the grid is not empty
    if grid.is_empty() {
        return Err(GetGridValueError::OutOfBounds);
    }

    // Convert row and col to usize safely
    let row_usize: usize = row.try_into().map_err(|_| GetGridValueError::OutOfBounds)?;
    let col_usize: usize = col.try_into().map_err(|_| GetGridValueError::OutOfBounds)?;

    // Check if row is within bounds
    if row_usize >= grid.len() {
        return Err(GetGridValueError::OutOfBounds);
    }

    // Check if col is within bounds for the given row
    if col_usize >= grid[row_usize].len() {
        return Err(GetGridValueError::OutOfBounds);
    }

    // Safely access the grid value
    Ok(grid[row_usize][col_usize])
}

#[derive(Error, Debug)]
enum TryMoveBoxError {
    #[error("Unexpected operation")]
    Unexpected(#[from] GetGridValueError),

    #[error("Hit the wall")]
    Wall
}


fn try_move_box(grid: &mut Grid, row: i32, col: i32, dir_row: i32, dir_col: i32) -> Result<(), TryMoveBoxError> {
    let (start_row, start_col) = (row, col);
    let (mut curr_row, mut curr_col) = (row, col);

    loop {
        curr_row += dir_row;
        curr_col += dir_col;

        let val = get_grid_value(grid, row, col)?;

        if val == '#' {
            return Err(TryMoveBoxError::Wall);
        }

        if val == '.' {
            swap(&mut grid[row as usize][col as usize], &mut grid[start_row as usize][start_col as usize]);
            return Ok(())
        }
    }
}

pub fn main() -> Result<(), AppError> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day15/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path)?;

    let (mut grid, start, movements) = parse_grid(content)?;

    let (mut row, mut col) = (start.0, start.1);
    for movement in movements {
        let (dir_row, dir_col) = movement_to_dir(movement)?;

        if grid[row as usize][col as usize] == '#' {
            row -= dir_row;
            col -= dir_col;
        }

        if grid[row as usize][col as usize] == 'O' {
            match try_move_box(&mut grid, row, col, dir_row, dir_col) {
                Ok(_) => {
                    row += dir_row;
                    col += dir_col;
                },
                Err(TryMoveBoxError::Wall) => {
                    row -= dir_row;
                    col -= dir_col;
                }
                _ => return Err(AppError::FailedToParseMovement(MovementToDirError::FailedToParseMovement))?
            }
        }
    }

    // println!("Part 1: {}", final_result);

    Ok(())
}
