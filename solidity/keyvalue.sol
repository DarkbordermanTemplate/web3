// SPDX-License-Identifier: UNLICENSED
pragma solidity^0.8.4;

error KeyAlreadyExists();

contract SmartContract {
    mapping(string => string) public map;

    function setValue(string memory key, string memory value) public {
        if (bytes(map[key]).length != 0){
            revert KeyAlreadyExists();
        }
        map[key] = value;
    }

    function getValue(string memory key) view public returns (string memory){
        return map[key];
    }
}
