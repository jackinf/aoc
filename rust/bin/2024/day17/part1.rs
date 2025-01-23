// #![allow(unused)]

use crate::prelude::*;
use log::debug;
use std::fs;
use std::fs::read_dir;

mod error;
mod prelude;
mod utils;

fn solve(program: Vec<u32>, mut reg_a: u32, mut reg_b: u32, mut reg_c: u32) -> Result<Vec<u32>> {
    let mut ins_ptr = 0;

    let combo_op = |op: u32, a: u32, b: u32, c: u32| -> Option<u32> {
        match op {
            0..=3 => Some(op),
            4 => Some(a),
            5 => Some(b),
            6 => Some(c),
            7 => None,
            _ => None,
        }
    };

    let mut output: Vec<u32> = vec![]; // todo: use it later

    while ins_ptr + 1 < program.len() {
        let opcode = *program.get(ins_ptr).ok_or(Error::GE())?;
        let operand = *program.get((ins_ptr + 1)).ok_or(Error::GE())?;

        match opcode {
            0 => {
                let val = combo_op(operand, reg_a, reg_b, reg_c).ok_or(Error::GE())?;
                reg_a /= u32::pow(2, val);
                ins_ptr += 2;
            }
            1 => {
                reg_b ^= operand;
                ins_ptr += 2;
            }
            2 => {
                reg_b = combo_op(operand, reg_a, reg_b, reg_c).ok_or(Error::GE())? % 8;
                ins_ptr += 2;
            }
            3 => {
                if reg_a != 0 && (operand as usize) < program.len() {
                    ins_ptr = operand as usize;
                } else {
                    ins_ptr += 2;
                }
            },
            4 => {
                reg_b ^= reg_c;
                ins_ptr += 2;
            }
            5 => {
                output.push(combo_op(operand, reg_a, reg_b, reg_c).ok_or(Error::GE())? % 8);
                ins_ptr += 2;
            }
            6 => {
                let val = combo_op(operand, reg_a, reg_b, reg_c).ok_or(Error::GE())?;
                reg_b = reg_a / u32::pow(2, val);
                ins_ptr += 2;
            }
            7 => {
                let val = combo_op(operand, reg_a, reg_b, reg_c).ok_or(Error::GE())?;
                reg_c = reg_a / u32::pow(2, val);
                ins_ptr += 2;
            }
            _ => panic!("not applicable"),
        }
    }

    if output.is_empty() {
        return Err(Error::GE());
    }

    Ok(output)
}

pub fn main() -> Result<()> {
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    let file_path = format!("{}/bin/2024/day17/input.txt", env!("CARGO_MANIFEST_DIR"));
    let content = fs::read_to_string(file_path)?;
    let content = content.replace("\r\n", "\n");
    let mut blocks = content.split("\n\n");

    debug!("{blocks:?}");

    let block1 = blocks.next().ok_or(Error::GE())?;
    let block2 = blocks.next().ok_or(Error::GE())?;

    debug!("{block1:?}");
    debug!("{block2:?}");

    let registers: Vec<u32> = block1
        .lines()
        .filter_map(|line| {
            line.split(":")
                .last()
                .map(str::trim)
                .and_then(|val| val.parse::<u32>().ok())
        })
        .collect();

    assert_eq!(registers.len(), 3);

    debug!("{registers:?}");

    let program: Vec<u32> = block2
        .split(": ")
        .last()
        .ok_or(Error::GE())?
        .split(",")
        .map(|val| val.parse::<u32>().map_err(|e| Error::GE()))
        .collect::<Result<Vec<_>>>()?;

    debug!("{program:?}");

    let result = solve(program, registers[0], registers[2], registers[2])?;

    let final_result: String = result
        .iter()
        .map(|val| val.to_string())
        .collect::<Vec<_>>()
        .join(",");

    println!("Part 1: {}", final_result);

    Ok(())
}
