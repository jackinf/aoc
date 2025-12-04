use log::{debug, info};

fn main() {
    env_logger::init();

    let contents: &str = include_str!("input.txt");
    let lines: Vec<&str> = contents.split("\n").collect();
    
    let mut result: u32 = 0;

    for line in lines {
        let nums: Vec<u32> = to_nums(&line);

        debug!("{:?}", nums);

        let biggest = get_biggest_num(&nums);
        debug!("BIGGEST NUM = {}", biggest);

        result += biggest;
    }

    info!("{}", result);
}

fn to_nums(line: &str) -> Vec<u32> {
    let nums: &Vec<u32> = &line.chars()
        .map(|ch| ch.to_digit(10).unwrap())
        .collect();

    nums.to_vec()
}

fn get_three_smallest_num(nums: &Vec<u32>) -> u32 {
    if nums.len() <= 1 {
        return 0
    }

    // find first biggest number pos
    let mut p1: usize = 0;
    let mut p1_best = 10;
    for candidate in 1..=9 {
        for i in 0..(nums.len() - 2) {
            if nums[i] < p1_best {
                p1_best = nums[i];
                p1 = i;
            }
        }
    }

    // now find the second biggest number after the first number
    let mut p2: usize = 0;
    let mut p2_best = 10;
    for candidate in 1..=9 {
        for i in (p1 + 1)..nums.len() - 1 {
            if nums[i] < p2_best {
                p2_best = nums[i];
                p2 = i;
            }
        }
    }

    // now find the second biggest number after the first number
    let mut p3: usize = 0;
    let mut p3_best = 10;
    for candidate in 1..=9 {
        for i in (p2 + 1)..nums.len() {
            if nums[i] < p3_best {
                p3_best = nums[i];
                p3 = i;
            }
        }
    }

    dbg!("P1 = {:?}", p1);
    dbg!("P2 = {:?}", p2);
    dbg!("P3 = {:?}", p3);

    p1_best * 100 + p2_best * 10 + p3_best
}

fn get_biggest_num(nums: &Vec<u32>) -> u32 {
    todo!()
}

#[cfg(test)]
mod tests {
    use super::*;

    use test_case::test_case;

    #[test_case("987654321111111", 111)]
    #[test_case("811111111111119", 111)]
    #[test_case("234234234234278", 232)] // TODO: not sure how to solve this now
    #[test_case("818181911112111", 111)]
    fn test_get_three_smallest_num(raw: &str, expected: u32) {
        let nums1: Vec<u32> = to_nums(raw);
        let res1 = get_three_smallest_num(&nums1);

        assert_eq!(res1, expected)
    }
}