use log::{debug, info};
use std::collections::VecDeque;

fn main() {
    env_logger::init();

    let contents = include_str!("sample0.txt");
    let groups: Vec<&str> = contents.split("\n\n").collect();
    let group0_raw = groups[0].split("\n").collect::<Vec<&str>>();

    let mut ranges = group0_raw.into_iter()
        .map(|item| {
            let parts = item.split("-").collect::<Vec<&str>>();
            let left = parts[0].parse::<u128>().unwrap();
            let right = parts[1].parse::<u128>().unwrap();

            (left, right)
        })
        .collect::<Vec<(u128, u128)>>();

    ranges.sort();

    // merge ranges
    let mut deque: VecDeque<(u128, u128)> = VecDeque::new();
    for (s1, e1) in ranges {
        if deque.is_empty() {
            deque.push_back((s1, e1));
            continue;
        }

        let (s2, e2) = deque.back_mut().unwrap();

        if *e2 >= s1 {
            *e2 = e1.max(*e2);
            continue;
        }

        if *s2 >= s1 {
            panic!("Should not happen");
        }

        if *e2 < s1 {
            deque.push_back((s1, e1));
            continue;
        }
    }

    debug!("{:?}", deque);

    let mut result = 0;

    for (start, end) in deque {
        result += end - start + 1;
    }

    info!("{result}");
}