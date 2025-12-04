use log::info;

fn main() {
    env_logger::init();

    let contents: &str = include_str!("input.txt");
    let grid: Vec<Vec<char>> = contents.split("\n")
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();

    dbg!("{:?}", grid[1][3]);

    let mut result: usize = 0;

    for row in 0..grid.len() {
        for col in 0..grid[0].len() {
            if grid[row][col] == '@' {
                if count_adjacent(&grid, row, col) < 4 {
                    result += 1;
                }
            }
        }
    }

    info!("{result}");
}

fn count_adjacent(grid: &Vec<Vec<char>>, row: usize, col: usize) -> usize {
    let mut adjacents: usize = 0;

    let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ];

    for (dr, dc)  in directions {
        if matches!(
            grid
                .get(row.wrapping_add_signed(dr))
                .and_then(|r| r.get(col.wrapping_add_signed(dc))),
            Some(&'@')
        ) {
            adjacents += 1;
        }
    }

    adjacents
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_adjacent() {
        let grid: Vec<Vec<char>> = vec!(
            vec!['.','.','@','@','.','@','@','@','@'],
            vec!['@','@','@','.','@','.','@','.','@']
        );

        assert_eq!(count_adjacent(&grid, 1, 1), 3);
    }
}