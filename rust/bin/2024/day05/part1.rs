use std::collections::{HashMap, HashSet};

fn parse_rules(block: &str) -> Result<HashMap<i32, HashSet<i32>>, &str> {
    block
        .split('\n')
        .map(|line| {
            let mut parts = line.split('|');

            let left = parts
                .next()
                .ok_or("Missing left part")?
                .parse::<i32>()
                .map_err(|_| "Invalid number for left part")?;

            let right = parts
                .next()
                .ok_or("Missing right part")?
                .parse::<i32>()
                .map_err(|_| "Invalid number for right part")?;

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
        })
}

fn parse_sections(block: &str) -> Result<Vec<Vec<i32>>, &str> {
    block
        .split('\n')
        .map(|line| {
            line.split(',')
                .map(|symbol| symbol.parse::<i32>().map_err(|_| "Invalid number"))
                .collect()
        })
        .collect::<Result<Vec<_>, _>>()
}


fn analyze_section(section: &Vec<i32>, rules: &HashMap<i32, HashSet<i32>>) -> i32 {
    for (i, &p1) in section.iter().enumerate() {
        for &p2 in &section[i + 1..] {
            if let Some(collection) = &rules.get(&p2) {
                if collection.contains(&p1) {
                    return 0;
                }
            }
        }
    }

    section[section.len() / 2]
}

pub fn main() -> Result<(), &'static str> {
    let content: &str = include_str!("input.txt");
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