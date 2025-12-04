use log::{debug, info};
use fancy_regex::Regex;

fn main() {
    env_logger::init();
    let contents: &str = include_str!("input.txt");
    let pairs: Vec<&str> = contents.split(",").collect();
    let re = init_regex();

    debug!("{:?}", pairs);

    let mut result: i64 = 0;

    for pair in pairs {
        let arr: Vec<&str> = pair.split("-").collect();
        let first = arr[0].parse::<i64>().unwrap();
        let last = arr[1].parse::<i64>().unwrap();

        debug!("FIST = {:?}, LAST = {:?}", first, last);

        for id in first..=last {
            if is_invalid(id, &re) {
                result += id;
            }
        }
    }

    info!("{}", result);
}

fn init_regex() -> Regex {
    Regex::new(r"^(.+)\1+$").unwrap()
}

fn is_invalid(id: i64, re: &Regex) -> bool {
    debug!("ID: {}", id);
    let id_str = id.to_string();
    
    re.is_match(&id_str).expect("REASON")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_invalid() {
        let re = init_regex();
       
        // Part 1
        assert_eq!(is_invalid(11, &re), true);
        assert_eq!(is_invalid(22, &re), true);
        assert_eq!(is_invalid(1010, &re), true);
        assert_eq!(is_invalid(1188511885, &re), true);
        assert_eq!(is_invalid(222222, &re), true);
        assert_eq!(is_invalid(446446, &re), true);
        assert_eq!(is_invalid(38593859, &re), true);
        assert_eq!(is_invalid(38593858, &re), false);
        assert_eq!(is_invalid(121, &re), false);
        assert_eq!(is_invalid(1, &re), false);

        // Part 2
        assert_eq!(is_invalid(123123123, &re), true);
        assert_eq!(is_invalid(2121212121, &re), true);
        assert_eq!(is_invalid(565656, &re), true);
        assert_eq!(is_invalid(824824824, &re), true);
    }
}