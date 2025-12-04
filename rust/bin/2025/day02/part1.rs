use log::{debug, info};

fn main() {
    env_logger::init();
    let contents: &str = include_str!("input.txt");

    let pairs: Vec<&str> = contents.split(",").collect();

    debug!("{:?}", pairs);

    let mut result: i64 = 0;

    for pair in pairs {
        let arr: Vec<&str> = pair.split("-").collect();
        let first = arr[0].parse::<i64>().unwrap();
        let last = arr[1].parse::<i64>().unwrap();

        debug!("FIST = {:?}, LAST = {:?}", first, last);

        for id in first..=last {
            if is_invalid(id) {
                result += id;
            }
        }
    }

    info!("{}", result);
}

fn is_invalid(id: i64) -> bool {
    debug!("ID: {}", id);
    let id_str = id.to_string();
    let id_len = id_str.len();
    if id_len % 2 == 1 {
        // i assume that odd id cannot be invalid
        return false
    }
    let left = &id_str[..id_len / 2];
    let right = &id_str[id_len / 2 ..];

    debug!("LEFT = {:?}", left);
    debug!("RIGHT = {:?}", right);

    left == right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_invalid() {
        assert_eq!(is_invalid(11), true);
        assert_eq!(is_invalid(22), true);
        assert_eq!(is_invalid(1010), true);
        assert_eq!(is_invalid(1188511885), true);
        assert_eq!(is_invalid(222222), true);
        assert_eq!(is_invalid(446446), true);
        assert_eq!(is_invalid(38593859), true);
        assert_eq!(is_invalid(38593858), false);
        assert_eq!(is_invalid(121), false);
        assert_eq!(is_invalid(1), false);
    }
}