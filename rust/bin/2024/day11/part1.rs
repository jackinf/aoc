use std::mem;

pub fn main() -> Result<(), String> {
    let content = include_str!("input.txt");

    let mut stones: Vec<i64> = content
        .split_whitespace()
        .map(|item| item.parse::<i64>().map_err(|_| "failed to parse integer".to_string()))
        .collect::<Result<Vec<i64>, String>>()?;

    for _ in 0..25 {
        let mut tmp: Vec<i64> = Vec::new();

        for &stone in stones.iter() {
            let stone_str = stone.to_string();
            let size = stone_str.len();

            if stone == 0 {
                tmp.push(1);
            } else if size % 2 == 0 {
                let (left, right) = stone_str.split_at(size / 2);
                // or:
                // let left: String = stone_str.chars().take(size / 2).collect();
                // let right: String = stone_str.chars().skip(size / 2).take(size / 2).collect();

                let left: i64 = left.parse::<i64>().map_err(|_| "failed to parse integer".to_string())?;
                let right: i64 = right.parse::<i64>().map_err(|_| "failed to parse integer".to_string())?;

                tmp.push(left);
                tmp.push(right);
            } else {
                tmp.push(stone * 2024);
            }
        }

        mem::swap(&mut tmp, &mut stones);
    }

    let final_result = stones.len();

    println!("Part 1: {}", final_result); // 187738

    Ok(())
}
