// Date: 25/05/22
// Runtime: 6 ms, faster than 7.14% of Rust online submissions for Bulls and Cows.
// Memory Usage: 2.2 MB, less than 21.43% of Rust online submissions for Bulls and Cows.
use std::collections::HashMap;

impl Solution {

    pub fn get_hint(secret: String, guess: String) -> String {

        pub fn check_bulls(secret_dictionary:&mut HashMap<char, i32>, guess_dictionary:&mut HashMap<char,i32>, secret: &String, guess: &String, bulls:&mut i32) -> (){
        for i in 0..secret.len(){
            if secret.as_bytes()[i] == guess.as_bytes()[i]{
                *bulls += 1;
                secret_dictionary.insert(secret.chars().nth(i).unwrap(), &secret_dictionary[&secret.chars().nth(i).unwrap()]-1);
                guess_dictionary.insert(guess.chars().nth(i).unwrap(), &guess_dictionary[&guess.chars().nth(i).unwrap()]-1 );
            }
        }
    }

        pub fn check_guess(secret_dictionary:&mut HashMap<char, i32>, guess_dictionary:&mut HashMap<char,i32>, secret: &String, guess: &String, cows:&mut i32) -> (){
        for i in secret.chars(){
            if secret_dictionary[&i] > 0 && guess_dictionary.contains_key(&i) && guess_dictionary[&i]>0{
                *cows += 1;
                secret_dictionary.insert(i, &secret_dictionary[&i]-1);
                guess_dictionary.insert(i, &guess_dictionary[&i]-1 );
            }
        }
    }

        let mut secret_hashmap:HashMap<char, i32> = HashMap::new();
        let mut guess_hashmap:HashMap<char, i32> = HashMap::new();
        let mut cows = 0;
        let mut bulls = 0;
        for i in secret.chars(){
            if secret_hashmap.contains_key(&i){
                secret_hashmap.insert(i, 1 + secret_hashmap[&i]);
            }
            else{
                secret_hashmap.insert(i,1 );
            }
        }
        for i in guess.chars(){
            if guess_hashmap.contains_key(&i){
                guess_hashmap.insert(i, 1 + guess_hashmap[&i]);
            }
            else{
                guess_hashmap.insert(i,1 );
            }
        }
        check_bulls(&mut secret_hashmap, &mut guess_hashmap, &secret, &guess, &mut bulls);
        check_guess(&mut secret_hashmap, &mut guess_hashmap, &secret, &guess, &mut cows);
        
        let result_string: String = format!("{}{}{}{}",&bulls.to_string().to_owned(),"A",&cows.to_string().to_owned(),"B" );
        result_string
    }
    
}