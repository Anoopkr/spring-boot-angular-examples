package com.spring.example.userportal.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.example.userportal.model.User;
import com.spring.example.userportal.repository.UserRepository;
import com.spring.example.userportal.service.UserService;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserRepository repository;

    @Override
    public User create(User user) {
        return repository.save(user);
    }

    @Override
    public User delete(String id) {
        User user = findById(id);
        if(user != null){
            repository.delete(user);
        }
        return user;
    }

    @Override
    public List findAll() {
        return repository.findAll();
    }

    @Override
    public User findById(String id) {
        return repository.findById(id);
    }

    @Override
    public User update(User user) {
        return null;
    }
}