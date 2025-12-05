use log::{debug, info};

fn main() {
    env_logger::init();

    let contents: &str = include_str!("input.txt");
    let lines: Vec<&str> = contents.split("\n").collect();
    
    let mut result: u64 = 0;

    for line in lines {
        let nums: Vec<u64> = to_nums(&line);

        debug!("{:?}", nums);

        let biggest = get_biggest_num(&nums, 12);
        debug!("BIGGEST NUM = {}", biggest);

        result += biggest;
    }

    info!("{}", result);
}

fn to_nums(line: &str) -> Vec<u64> {
    let nums: &Vec<u64> = &line.chars()
        .map(|ch| u64::from(ch.to_digit(10).unwrap()))
        .collect();

    nums.to_vec()
}

fn get_biggest_num(nums: &Vec<u64>, count: usize) -> u64 {    
    let mut result: u64 = 0;
    let mut start_pos = 0;
    
    for position in 0..count {
        let remaining_needed = count - position - 1;        
        let search_end = nums.len() - remaining_needed;
        
        let mut best_digit = 0;
        let mut best_pos = start_pos;
        
        for i in start_pos..search_end {
            if nums[i] > best_digit {
                best_digit = nums[i];
                best_pos = i;
            }
        }
        
        result *= 10;
        result += best_digit;
        start_pos = best_pos + 1;
    }
    
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    use test_case::test_case;

    #[test_case("987654321111111", 987654321111)]
    #[test_case("811111111111119", 811111111119)]
    #[test_case("234234234234278", 434234234278)]
    #[test_case("818181911112111", 888911112111)]
    fn test_get_biggest_num(raw: &str, expected: u64) {
        let nums1: Vec<u64> = to_nums(raw);
        let res1 = get_biggest_num(&nums1, 12);

        assert_eq!(res1, expected)
    }
}