use std::collections::{HashMap, HashSet};

fn parse_rules(block1: &str) -> Result<HashMap<i32, HashSet<i32>>, String> {
    let rules: Result<HashMap<i32, HashSet<i32>>, String> = block1
        .split('\n')
        .map(|line| {
            let mut parts = line.split('|');

            let left = parts
                .next()
                .ok_or("Missing left part".to_string())
                .and_then(|s| {
                    s.parse::<i32>()
                        .map_err(|_| "Invalid number for left part".to_string())
                })?;

            let right = parts
                .next()
                .ok_or("Missing right part".to_string())
                .and_then(|s| {
                    s.parse::<i32>()
                        .map_err(|_| "Invalid number for right part".to_string())
                })?;

            Ok((left, right))
        })
        .collect::<Result<Vec<_>, _>>()
        .map(|pairs| {
            pairs
                .into_iter()
                .fold(HashMap::new(), |mut acc, (left, right)| {
                    acc.entry(left).or_insert_with(HashSet::new).insert(right);
                    acc
                })
        });
    rules
}

fn parse_sections(block2: &str) -> Result<Vec<Vec<i32>>, String> {
    let sections: Result<Vec<Vec<i32>>, String> = block2
        .split('\n')
        .map(|line| {
            line.split(',')
                .map(|symbol| {
                    symbol
                        .parse::<i32>()
                        .map_err(|_| "Invalid number".to_string())
                })
                .collect()
        })
        .collect::<Result<Vec<_>, _>>();
    sections
}

fn analyze_section(section: &Vec<i32>, rules: &HashMap<i32, HashSet<i32>>) -> i32 {
    for i in 0..section.len() - 1 {
        for j in i..section.len() {
            let p1: i32 = section[i];
            let p2: i32 = section[j];

            if let Some(collection) = &rules.get(&p2) {
                if collection.contains(&p1) {
                    return 0;
                }
            }
        }
    }

    section[section.len() / 2]
}

pub fn main() -> Result<(), String> {
    let content: String = include_str!("input.txt").to_string();
    let mut blocks = content.split("\n\n");

    let block1 = blocks.next().ok_or("Missing block 1")?;
    let block2 = blocks.next().ok_or("Missing block 2")?;

    let rules = parse_rules(block1)?;
    let sections = parse_sections(block2)?;

    let final_result: i32 = sections
        .iter()
        .map(|section| analyze_section(&section, &rules))
        .sum();

    println!("Part 1: {}", final_result);

    Ok(())
}
