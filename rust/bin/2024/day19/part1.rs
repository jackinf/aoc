use crate::prelude::*;
use std::collections::HashMap;
use std::fs;

mod error;
mod prelude;

type Patterns = Vec<String>;
type Design = String;
type Designs = Vec<Design>;

fn parse_content(content: &str) -> Result<(Patterns, Designs)> {
    let mut blocks = content.split("\n\n");

    let patterns = blocks
        .next()
        .ok_or(Error::NA)?
        .lines()
        .next()
        .ok_or(Error::NA)?
        .split(", ")
        .map(|x| x.trim().to_string())
        .collect::<Vec<String>>();

    let designs = blocks
        .next()
        .ok_or(Error::NA)?
        .lines()
        .map(|x| x.to_string())
        .collect::<Vec<String>>();

    Ok((patterns, designs))
}

fn check_match(cache: &mut HashMap<String, bool>, patterns: &[String], design: &str) -> bool {
    if let Some(&cached_result) = cache.get(design) {
        return cached_result;
    }

    if design.is_empty() {
        cache.insert(design.to_string(), true);
        return true;
    }

    for pattern in patterns {
        if design.starts_with(pattern) {
            let rest = &design[pattern.len()..];
            if check_match(cache, patterns, rest) {
                cache.insert(design.to_string(), true);
                return true;
            }
        }
    }

    cache.insert(design.to_string(), false);
    false
}

fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day19/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path).map_err(|e| Error::NA)?;
    let content = content.replace("\r\n", "\n");

    let (patterns, designs) = parse_content(&content)?;

    let mut matches = 0;
    let mut cache: HashMap<String, bool> = HashMap::new();

    for design_val in designs.iter() {
        if check_match(&mut cache, &patterns, design_val) {
            matches += 1;
        }
    }

    println!("Part 1: {}", matches);
    Ok(())
}
