// https://github.com/hasanghorbel/aoc-2024/blob/master/day04/src/part1/mod.rs
pub fn main() {
    let input: Vec<Vec<char>> = include_str!("sample1.txt")
        .lines()
        .map(|line| line.chars().collect())
        .collect();
    let target = ['M', 'A', 'S'];

    let height = input.len();
    let width = input.first().unwrap().len();
    let mut ans = 0;
    for i in 0..height {
        for j in 0..width {
            if input[i][j] != 'X' {
                continue;
            }

            if j > 2 && input[i][j - 3..j] == ['S', 'A', 'M'] {
                ans += 1;
            }
            if j < width - 3 && input[i][j + 1..j + 4] == target {
                ans += 1;
            }
            if i > 2 && (1..4).all(|k| input[i - k][j] == target[k - 1]) {
                ans += 1;
            }
            if i < height - 3 && (1..4).all(|k| input[i + k][j] == target[k - 1]) {
                ans += 1;
            }
            if i > 2 && j > 2 && (1..4).all(|k| input[i - k][j - k] == target[k - 1]) {
                ans += 1;
            }
            if i < height - 3 && j > 2 && (1..4).all(|k| input[i + k][j - k] == target[k - 1]) {
                ans += 1;
            }
            if i > 2 && j < width - 3 && (1..4).all(|k| input[i - k][j + k] == target[k - 1]) {
                ans += 1;
            }
            if i < height - 3
                && j < width - 3
                && (1..4).all(|k| input[i + k][j + k] == target[k - 1])
            {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}