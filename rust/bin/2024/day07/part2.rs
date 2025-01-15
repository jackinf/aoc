use std::collections::VecDeque;
use std::time::Instant;

pub fn main() -> Result<(), String> {
    let content: String = include_str!("input.txt").to_string();
    let timer = Instant::now();

    let mut final_result = 0;
    for line in content.lines() {
        let mut split_line = line.split(':');
        let left = split_line
            .next()
            .unwrap()
            .parse::<i64>()
            .unwrap_or_else(|_| panic!("Failed to parse"));
        let right: Vec<i64> = split_line
            .next()
            .unwrap()
            .split_whitespace()
            .map(|num| num.parse::<i64>().unwrap())
            .collect();

        let mut queue: VecDeque<(i64, i64)> = VecDeque::new();
        queue.push_back((1, right[0]));

        while !queue.is_empty() {
            let (right_index, answer) = queue.pop_front().unwrap();
            if answer > left {
                continue;
            }

            if right_index as usize == right.len() {
                if answer == left {
                    final_result += answer;
                    break;
                }
                continue;
            }

            queue.push_back((right_index + 1, answer + right[right_index as usize]));
            queue.push_back((right_index + 1, answer * right[right_index as usize]));

            let comb1 = format!("{}{}", answer, right[right_index as usize])
                .parse::<i64>()
                .unwrap();
            queue.push_back((right_index + 1, comb1));
        }
    }

    println!("Part 2: {}", final_result); // 165278151522644

    println!("Time: {:?}", timer.elapsed());

    Ok(())
}
