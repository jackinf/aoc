pub fn parse_grid(content: &str) -> Vec<Vec<char>> {
    content
        .lines() // Use `lines()` to handle splitting into lines
        .map(|line| line.chars().collect())
        .collect()
}

pub fn get_start(grid: &[Vec<char>]) -> Result<(i32, i32), String> {
    grid.iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter().enumerate().filter_map(move |(j, &ch)| {
                if ch == '^' {
                    Some((i as i32, j as i32))
                } else {
                    None
                }
            })
        })
        .next() // Get the first matching element
        .ok_or_else(|| "No start found".to_string())
}
