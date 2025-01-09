use std::collections::{HashMap, HashSet};

pub fn parse_rules(block: &str) -> Result<HashMap<i32, HashSet<i32>>, &str> {
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

pub fn parse_sections(block: &str) -> Result<Vec<Vec<i32>>, &str> {
    block
        .split('\n')
        .map(|line| {
            line.split(',')
                .map(|symbol| symbol.parse::<i32>().map_err(|_| "Invalid number"))
                .collect()
        })
        .collect::<Result<Vec<_>, _>>()
}
