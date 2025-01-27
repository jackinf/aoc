// #![allow(unused)]

use crate::prelude::*;
use log::debug;
use std::fs;
use std::fs::read_dir;

mod error;
mod prelude;

type Patterns = Vec<String>;
type Design = String;
type Designs = Vec<Design>;

fn parse_content(content: &str) -> Result<(Patterns, Designs)> {
    let mut blocks = content.split("\n\n");

    let first = blocks
        .next()
        .ok_or(Error::NA)?
        .lines()
        .next()
        .ok_or(Error::NA)?
        .split(",")
        .map(|x| x.trim().to_string())
        .collect::<Patterns>();

    let second = blocks
        .next()
        .ok_or(Error::NA)?
        .lines()
        .map(|line| line.to_string())
        .collect::<Designs>();

    Ok((first, second))
}

fn check_match(patterns: &Patterns, design: Design) -> bool {
    if design == "" {
        return true;
    }

    for pattern in patterns {
        if design.starts_with(pattern) {
            let size = pattern.len();
            let rest = design[size..].to_string();
            let matched = check_match(&patterns, rest);

            if matched {
                return true;
            }
        }
    }

    false
}

pub fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day19/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path).map_err(|e| Error::NA)?;
    let content = content.replace("\r\n", "\n");

    let (patterns, designs) = parse_content(&content)?;

    let mut matches = 0;
    for design_val in designs {
        let matched = check_match(&patterns, design_val);
        if matched {
            matches += 1;
        }
    }

    // debug!("{patterns:?}");
    // debug!("{designs:?}");

    println!("Part 1: {}", matches);

    Ok(())
}
