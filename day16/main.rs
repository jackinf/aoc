// convert main.py to Rust

use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("day16/input.txt").unwrap();
    let reader = BufReader::new(file);
    let mut lines = reader.lines();

    // loop lines
    lines.for_each(|line| {
        let line = line.unwrap();
        let mut parts = line.split("ö ");
        let field = parts.next().unwrap();
        let ranges = parts.next().unwrap();
        let mut ranges = ranges.split(" or ");
        let mut range1 = ranges.next().unwrap().split("-");
        let mut range2 = ranges.next().unwrap().split("-");
        let range1 = (range1.next().unwrap().parse::<u32>().unwrap(), range1.next().unwrap().parse::<u32>().unwrap());
        let range2 = (range2.next().unwrap().parse::<u32>().unwrap(), range2.next().unwrap().parse::<u32>().unwrap());
        println!("field: {}, range1: {:?}, range2: {:?}", field, range1, range2);
    });
}