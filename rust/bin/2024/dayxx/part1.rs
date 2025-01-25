// #![allow(unused)]

use std::fs::read_dir;
use crate::prelude::*;

mod error;
mod prelude;
mod utils;

pub fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/dayxx/input.txt", env!("CARGO_MANIFEST_DIR"));

    for entry in read_dir("./")?.filter_map(|e| e.ok()) {
        let entry: String = W(&entry).try_into()?;
        println!("{entry:?}")
    };

    // println!("Part 1: {}", final_result);
}