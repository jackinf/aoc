use std::collections::{HashMap, HashSet};

mod common;

use common::parse_rules;
use common::parse_sections;

fn is_valid_section(section: &[i32], rules: &HashMap<i32, HashSet<i32>>) -> bool {
    for (i, p1) in section.iter().enumerate() {
        for p2 in &section[i + 1..] {
            if let Some(collection) = rules.get(p2) {
                if collection.contains(p1) {
                    return false;
                }
            }
        }
    }

    true
}

fn fix_section_v2(section: &mut [i32], rules: &HashMap<i32, HashSet<i32>>) -> i32 {
    for i in 0..section.len() {
        for j in (i + 1)..section.len() {
            let p1 = &section[i];
            let p2 = &section[j];
            if let Some(collection) = rules.get(p2) {
                if collection.contains(p1) {
                    section.swap(i, j);
                }
            }
        }
    }

    section[section.len() / 2]
}

#[allow(dead_code)]
fn fix_section_v1(section: &mut [i32], rules: &HashMap<i32, HashSet<i32>>) -> i32 {
    for i in 0..section.len() {
        for j in (i + 1)..section.len() {
            if let Some(collection) = rules.get(&section[j]) {
                if collection.contains(&section[i]) {
                    section.swap(i, j);
                }
            }
        }
    }

    section[section.len() / 2]
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let content: &str = include_str!("input.txt");
    let mut blocks = content.split("\n\n");

    let block1 = blocks.next().ok_or("Missing block 1")?;
    let block2 = blocks.next().ok_or("Missing block 2")?;

    let rules = parse_rules(block1)?;
    let mut sections = parse_sections(block2)?;

    let final_result: i32 = sections
        .iter_mut()
        .filter(|section| !is_valid_section(section, &rules))
        .map(|section| fix_section_v2(section, &rules))
        .sum();

    println!("Part 2: {}", final_result);

    Ok(())
}
