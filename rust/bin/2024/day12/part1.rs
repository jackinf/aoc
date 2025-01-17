use std::collections::{HashMap, HashSet};

type Wall = (i32, i32, i32, i32);
type AllWalls = HashMap<String, HashSet<Wall>>;

fn read_grid(content: &str) -> Vec<Vec<char>> {
    content.lines().map(|row| row.chars().collect()).collect()
}

fn toggle_wall(wall: &Wall, key: String, all_walls: &mut AllWalls) {
    let walls = all_walls.entry(key).or_default();
    if walls.contains(wall) {
        walls.remove(wall);
    } else {
        walls.insert(*wall);
    }
}

fn solve(
    row: i32,
    col: i32,
    symbol: char,
    key: String,
    grid: &mut Vec<Vec<char>>,
    all_walls: &mut AllWalls,
) -> Option<i32> {
    let width = grid.first()?.len() as i32;
    let height = grid.len() as i32;
    let empty = '.';
    let directions: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, 1), (0, -1)];

    if 0 > row || 0 > col || height <= row || width <= col {
        return None;
    }

    // if let _ = grid.get(row as usize)
    //     .and_then(|row_vec| row_vec.get(col as usize))
    //     .map_or(false, |&val| val != symbol) {
    //     return None;
    // }
    //
    // if let Some(cell) = grid.get_mut(row as usize).and_then(|row_vec| row_vec.get_mut(col as usize)) {
    //     *cell = empty;
    // }

    match grid
        .get_mut(row as usize)
        .and_then(|row_vec| row_vec.get_mut(col as usize))
    {
        Some(item) if *item == symbol => *item = empty,
        _ => return None,
    }

    // if row < 0 || col < 0 || row >= height || col >= width {
    //     return None;
    // }
    //
    // if grid[row as usize][col as usize] != symbol {
    //     return None;
    // }
    //
    // grid[row as usize][col as usize] = empty;

    // Define walls
    let walls = [
        (row, col, row + 1, col),
        (row, col, row, col + 1),
        (row, col + 1, row + 1, col + 1),
        (row + 1, col, row + 1, col + 1),
    ];

    for wall in walls {
        toggle_wall(&wall, key.clone(), all_walls);
    }

    let mut areas_count = 1;
    for (dr, dc) in directions {
        if let Some(res) = solve(row + dr, col + dc, symbol, key.clone(), grid, all_walls) {
            areas_count += res;
        }
    }

    Some(areas_count)
}

fn calculate_result(areas: &HashMap<String, i32>, all_walls: AllWalls) -> i32 {
    let mut result = 0;
    for (key, &areas_count) in areas.iter() {
        if let Some(walls) = all_walls.get(key) {
            result += areas_count * walls.len() as i32;
        }
    }

    result
}

pub fn main() -> Result<(), String> {
    let content = include_str!("./input.txt");

    // read grid
    let mut grid: Vec<Vec<char>> = read_grid(content);
    let width = grid.first().ok_or("no such element".to_string())?.len();
    let height = grid.len();

    let mut all_walls: AllWalls = HashMap::default();
    let mut areas: HashMap<String, i32> = Default::default();

    for row in 0..height {
        for col in 0..width {
            let symbol = grid[row][col];
            if symbol != '.' {
                let key = format!("{}{}", row * 100000 + col, symbol);
                if let Some(areas_count) = solve(
                    row as i32,
                    col as i32,
                    symbol,
                    key.clone(),
                    &mut grid,
                    &mut all_walls,
                ) {
                    areas.entry(key).or_insert_with(|| areas_count);
                }
            }
        }
    }

    let final_result = calculate_result(&areas, all_walls);

    println!("Part 1: {}", final_result); // 1370100

    Ok(())
}
