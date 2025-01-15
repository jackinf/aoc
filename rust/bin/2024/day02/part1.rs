pub fn main() {
    let contents = include_str!("input.txt");
    let lines: Vec<_> = contents.split('\n').collect();
    let mut safe_count = 0;

    for line in lines {
        let nums: Vec<_> = line
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap())
            .collect();

        let mut safe_asc = true;
        let mut safe_desc = true;

        for i in 1..nums.len() {
            let diff = nums[i] - nums[i - 1];
            if !(1..=3).contains(&diff) {
                safe_asc = false;
                break;
            }
        }

        for i in 1..nums.len() {
            let diff = nums[i] - nums[i - 1];
            if !(-3..=-1).contains(&diff) {
                safe_desc = false;
                break;
            }
        }

        if safe_asc || safe_desc {
            safe_count += 1;
        }
    }

    println!("Part 1: {}", safe_count);
}
