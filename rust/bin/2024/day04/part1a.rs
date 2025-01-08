use std::error::Error;
use log::debug;

pub fn main() -> Result<(), Box<dyn Error>> {
    let input: String = include_str!("sample1.txt").to_string();

    let lines: Vec<_> = input.split('\n').collect();

    let grid: Vec<Vec<char>> = lines.iter().map(|item| item.chars().collect()).collect();
    let rows_count: usize = grid.len();
    let cols_count: usize = grid.get(0).unwrap().len();

    // println!("{:?}", grid);
    println!("rows_count: {}, cols_count: {}", rows_count, cols_count);

    let get_at = |row: usize, col: usize| {
        grid.get(row).and_then(|r| r.get(col)).copied()
    };

    let mut score = 0;
    for row in 0..rows_count-3 {
        for col in 0..cols_count-3 {

            let c00 = get_at(row, col).unwrap();
            let c01 = get_at(row, col + 1).unwrap();
            let c02 = get_at(row, col + 2).unwrap();
            let c03 = get_at(row, col + 3).unwrap();
            let c10 = get_at(row + 1, col).unwrap();
            let c20 = get_at(row + 2, col).unwrap();
            let c30 = get_at(row + 3, col).unwrap();

            // let mut level1: Vec<char> = vec![];

            // if res == 'X' {
            //     if get_at(row - 1, col).unwrap() == 'M' && get_at(row - 2, col).unwrap() == 'A' && get_at(row - 3, col).unwrap() == 'S' {
            //         score += 1;
            //     }
            // }

            // for drow in [-1, 0, 1] {
            //     for dcol in [-1, 0, 1] {
            //         if drow == 0 && dcol == 0 {
            //             continue;
            //         }
            //
            //         let nrow = row as isize + drow;
            //         let ncol = col as isize + dcol;
            //
            //         if nrow >= 0 && nrow < rows_count as isize && ncol >= 0 && ncol < cols_count as isize {
            //             if let Some(val) = get_at(nrow as usize, ncol as usize) {
            //                 level1.push(val);
            //             }
            //         }
            //     }
            // }

            println!("{:?}", level1);
        }
    }

    // println!("Part 1: {}", final_result);

    Ok(())
}