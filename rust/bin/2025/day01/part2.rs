const DEBUG: bool = false;

fn div_floor(a: i32, b: i32) -> i32 {
    if a >= 0 {
        a / b
    } else {
        (a - b + 1) / b
    }
}

fn div_ceil(a: i32, b: i32) -> i32 {
    if a >= 0 {
        (a + b - 1) / b
    } else {
        a / b
    }
}

fn main() {
    let content: &str = include_str!("input.txt");

    let lines: Vec<&str> = content.split("\n").collect();
    let mut current: i32 = 50;
    let mut password: i32 = 0;

    for line in lines {
        if line.is_empty() {
            continue;
        }
        
        let dir: &str = &line[..1];
        let rotations: i32 = line[1..].parse::<i32>().unwrap();

        if rotations == 0 {
            continue;
        }

        if dir == "L" {
            let first = current - rotations;
            let last = current - 1;
            
            let lo = div_ceil(first, 100);
            let hi = div_floor(last, 100);
            
            if hi >= lo {
                password += hi - lo + 1;
            }
            
            current = (current - rotations).rem_euclid(100);
        } else {
            let first = current + 1;
            let last = current + rotations;
            
            let lo = div_ceil(first, 100);
            let hi = div_floor(last, 100);
            
            if hi >= lo {
                password += hi - lo + 1;
            }
            
            current = (current + rotations).rem_euclid(100);
        }
    }

    println!("{}", password);
}