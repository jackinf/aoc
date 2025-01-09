pub fn main() {
    let content = include_str!("input.txt");

    let re = regex::Regex::new(r"mul\(\d+,\d+\)").unwrap();
    let groups: Vec<_> = re.find_iter(content).collect();

    let mut final_result = 0;
    for group in groups {
        let group_str = group.as_str();
        let values_str = group_str[4..group_str.len() - 1]
            .split(',')
            .collect::<Vec<_>>();
        let val1 = values_str[0].parse::<i32>().unwrap();
        let val2 = values_str[1].parse::<i32>().unwrap();

        let result = val1 * val2;
        final_result += result;
    }

    println!("Part 1: {}", final_result);
}
