// https://github.com/hasanghorbel/aoc-2024/blob/master/day04/src/part2/mod.rs
pub fn main() {
    let input: Vec<Vec<char>> = include_str!("../input.txt")
        .lines()
        .map(|line| line.chars().collect())
        .collect();
    let height = input.len();
    let width = input.first().unwrap().len();
    let mut ans = 0;
    for i in 1..height - 1 {
        for j in 1..width - 1 {
            if input[i][j] != 'A' {
                continue;
            }

            if (input[i - 1][j - 1] == 'M' && input[i + 1][j + 1] == 'S'
                || input[i - 1][j - 1] == 'S' && input[i + 1][j + 1] == 'M')
                && (input[i - 1][j + 1] == 'M' && input[i + 1][j - 1] == 'S'
                    || input[i - 1][j + 1] == 'S' && input[i + 1][j - 1] == 'M')
            {
                ans += 1;
            }
        }
    }
    println!("Part 2: {}", ans);
}
