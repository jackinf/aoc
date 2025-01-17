use log::debug;
use std::collections::HashMap;

pub fn main() {
    let content = include_str!("sample1.txt").to_string();
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();

    let line: Vec<char> = content.chars().take(content.len() - 1).collect();

    println!("line");
    debug!("{:?}", line);

    // parsing
    let mut spaces = HashMap::new();
    let mut files = HashMap::new();
    let mut index = 0;
    let mut id: i32 = -1;

    while index < line.len() {
        id += 1;
        files.insert(id, line[index].to_digit(10).unwrap());
        index += 1;

        if index < line.len() {
            spaces.insert(id, line[index].to_digit(10).unwrap());
            index += 1;
        }
    }

    let (_, last_val) = spaces.iter_mut().last().unwrap();
    *last_val = 0;

    println!("Spaces");
    debug!("{:?}", spaces);

    println!("Files");
    debug!("{:?}", files);

    // process_files_and_spaces
    let mut results = vec![];
    let mut files_pointer = id;
    let mut id = -1;

    while id < files_pointer {
        if files[&files_pointer] == 0 {
            files.remove(&files_pointer);
            files_pointer -= 1;
            continue;
        }

        if spaces[&id] == 0 {
            spaces.remove(&id);
            id += 1;
            for _ in 0..files[&id] {
                results.push(id);
            }
            continue;
        }

        files.insert(files_pointer, files[&files_pointer] - 1);
        spaces.insert(id, spaces[&id] - 1);
        results.push(files_pointer);
    }

    // calculate final result
    // let final_result = results.iter().enumerate().map(|(i, val)| i as i32 * val).fold(|acc, val| acc + val, 0);

    let final_result: i32 = results
        .iter()
        .enumerate()
        .map(|(i, val)| i as i32 * val)
        .sum();

    println!("Part 1: {}", final_result);
}
