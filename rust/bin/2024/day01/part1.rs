use log::debug;

fn main() {
    let contents = include_str!("input.txt");

    let split: Vec<_> = contents.split('\n').collect();

    let mut lefts: Vec<i32> = Vec::new();
    let mut rights: Vec<i32> = Vec::new();

    for line in split {
        debug!("{}", line);

        let line_parts: Vec<_> = line.split_whitespace().collect();
        assert_eq!(line_parts.len(), 2);

        let left = line_parts[0];
        let right = line_parts[1];

        let left_num: i32 = left.parse().unwrap();
        let right_num: i32 = right.parse().unwrap();

        lefts.push(left_num);
        rights.push(right_num);
    }

    lefts.sort();
    rights.sort();

    let mut final_result = 0;
    for i in 0..lefts.len() {
        let left = lefts[i];
        let right = rights[i];
        let result = (left - right).abs();
        final_result += result;
    }

    println!("Part 1: {}", final_result);
}
