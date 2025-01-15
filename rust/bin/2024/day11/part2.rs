use std::collections::HashMap;
use std::mem;

fn next_stone(&stone: &i64) -> Result<Vec<i64>, String> {
    if stone == 0 {
        return Ok(vec![1]);
    }

    let stone_str = stone.to_string();
    let size = stone_str.len();
    if size % 2 == 0 {
        let (left, right) = stone_str.split_at(size / 2);

        return Ok(vec![
            left.parse::<i64>().map_err(|_| "failed to parse")?,
            right.parse::<i64>().map_err(|_| "failed to parse")?,
        ]);
    }

    Ok(vec![stone * 2024])
}

fn next_state(arrangement: &HashMap<i64, i64>) -> Result<HashMap<i64, i64>, String> {
    let mut new_arrangement: HashMap<i64, i64> = HashMap::new();

    for (stone, &count) in arrangement {
        let new_stones = next_stone(stone)?;

        for new_stone in new_stones {
            *new_arrangement.entry(new_stone).or_insert(0) += count;
        }
    }

    Ok(new_arrangement)
}

pub fn main() -> Result<(), String> {
    let content = include_str!("./input.txt");
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();

    let mut stones: Vec<i64> = content
        .split_whitespace()
        .map(|item| {
            item.parse::<i64>()
                .map_err(|_| "failed to parse".to_string())
        })
        .collect::<Result<Vec<i64>, String>>()?;

    let mut coll: HashMap<i64, i64> = stones.into_iter().fold(HashMap::new(), |mut acc, stone| {
        acc.entry(stone).or_insert_with(|| 1);
        acc
    });

    for _ in 0..75 {
        let mut new_stones = next_state(&coll)?;
        mem::swap(&mut coll, &mut new_stones);
    }

    let final_result = coll.values().fold(0, |mut acc, curr| {
        acc += curr;
        acc
    });

    println!("Part 2: {}", final_result); //  223767210249237

    Ok(())
}
