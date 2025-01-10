pub fn main() -> Result<(), String> {
    let content = include_str!("sample1.txt");

    let grid: Vec<Vec<char>> = content
        .lines() // Use `lines()` to handle splitting into lines
        .map(|line| line.chars().collect())
        .collect();

    // Find the starting position ('^') in the grid
    let start: (usize, usize) = grid
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter()
                .enumerate()
                .filter_map(move |(j, &ch)| if ch == '^' { Some((i, j)) } else { None })
        })
        .next() // Get the first matching element
        .ok_or_else(|| "No start found".to_string())?; // Convert None to an error

    println!("Start position: {:?}", start);

    let final_result = 0; // Placeholder for actual logic
    println!("Part 1: {}", final_result);

    Ok(())
}
