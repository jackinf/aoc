use std::collections::{HashMap, HashSet};

mod common;

use common::parse_rules;
use common::parse_sections;

fn analyze_section(section: &[i32], rules: &HashMap<i32, HashSet<i32>>) -> i32 {
    for (i, p1) in section.iter().enumerate() {
        for p2 in &section[i + 1..] {
            if let Some(collection) = rules.get(p2) {
                if collection.contains(p1) {
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
        .map(|section| analyze_section(section, &rules))
        .sum();

    println!("Part 1: {}", final_result);

    Ok(())
}
