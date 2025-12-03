const DEBUG: bool = false;

fn main() {
    let content: &str = include_str!("input.txt");

    let lines: Vec<&str> = content.split("\n").collect();
    let mut current: i32 = 50;
    let mut password: i32 = 0;

    for line in lines {
        let dir: &str = &line[..1];
        let rotations: &i32 = &line[1..].parse::<i32>().unwrap();

        if dir == "L" {
            current -= rotations;

            while current < 0 {
                current += 100;
            }
        } else if dir == "R" {
            current += rotations;
            
            while current >= 100 {
                current -= 100;
            }
        }

        if current == 0 {
            password += 1;
        }

        if DEBUG {
            print!("DIR = {}, ", dir);
            print!("ROTATIONS = {}, ", rotations);
            print!("CURRENT = {}, ", current);
            print!("SCORE = {}", password);
            println!();
        }
    }

    print!("{}", password);
}