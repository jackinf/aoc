pub fn main() {
    let content = include_str!("input.txt");

    let re = regex::Regex::new(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))").unwrap();
    let groups: Vec<_> = re.find_iter(content).collect();

    let mut final_result = 0;
    let mut enabled = true;
    for group in groups {
        let group_str = group.as_str();
        let operation = group_str.split('(').collect::<Vec<_>>()[0];

        match operation {
            "do" => enabled = true,
            "don't" => enabled = false,
            "mul" => {
                if enabled {
                    let values_str = group_str[4..group_str.len() - 1]
                        .split(',')
                        .collect::<Vec<_>>();
                    let val1 = values_str[0].parse::<i32>().unwrap();
                    let val2 = values_str[1].parse::<i32>().unwrap();

                    let result = val1 * val2;
                    final_result += result;
                }
            }
            _ => {}
        }
    }

    println!("Part 2: {}", final_result);
}
