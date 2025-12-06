use log::{debug, info};

fn main() {
    env_logger::init();

    let contents = include_str!("input.txt");
    let grid: Vec<Vec<char>> = contents
        .lines()
        .map(|line| line.chars().collect())
        .collect();
    // debug!("GRID = {:?}", grid);

    let last_row = grid.len() - 1;
    let mut op_indices_start: Vec<usize> = vec![];
    let mut op_indices_end: Vec<usize> = vec![];
    for col in 0..grid[0].len() {
        // let col_len = grid[0].len();
        // debug!("OP INDEXES. COL = {col} COL_LEN = {col_len}");
        let therow = &grid[last_row];
        let val = therow[col];
        // debug!("VAL = {val}");
        if val != ' ' {
            op_indices_start.push(col);
            if col >= 1 {
                op_indices_end.push(col - 1);
            }
        } 
    }
    op_indices_end.push(grid[0].len() - 1);

    assert_eq!(op_indices_start.len(), op_indices_end.len());
    
    // debug!("START OP INDICES = {:?}", op_indices_start);
    // debug!("END OP INDICES = {:?}", op_indices_end);

    let mut result: u64 = 0;

    for op_index in 0..op_indices_start.len() {
        let op_index_start = op_indices_start[op_index];
        let op_index_end = op_indices_end[op_index];

        let mut numbers: Vec<u64> = vec![];
        for col in (op_index_start..=op_index_end).rev() {
            let mut number_chars: Vec<char> = vec![];
            for row in 0..grid.len() - 1 {
                // debug!("ROW {row} AND COL {col}");
                if grid[row][col] != ' ' {
                    number_chars.push(grid[row][col]);
                }
            }

            // if all spaces collected
            if number_chars.is_empty() {
                continue;
            }

            // debug!("number_chars = {number_chars:?}");
            let number_str: String = number_chars.iter().collect();
            // debug!("number_str = {number_str}");
            let number = number_str.parse::<u64>().expect("should have collected a valid number");
            // debug!("number = {number}");
            numbers.push(number);
        }

        info!("COLLECTED = {numbers:?}");

        if grid[grid.len() - 1][op_index_start] == '*' {
            let product: u64 = numbers.iter().product();
            debug!("PRODUCT = {product}");
            result += product;
        } else if grid[grid.len() - 1][op_index_start] == '+' {
            let sum: u64 = numbers.iter().sum();
            debug!("SUM = {sum}");
            result += sum;
        }

        info!("RESULT = {result}");
    }
}
