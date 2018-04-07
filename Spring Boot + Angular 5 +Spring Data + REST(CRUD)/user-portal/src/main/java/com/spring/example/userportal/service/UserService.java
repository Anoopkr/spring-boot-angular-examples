package com.spring.example.userportal.service;

import java.util.List;

import com.spring.example.userportal.model.User;

public interface UserService {

	 public User create(User user);
	 public User delete(String id);
	 public List findAll();
	 public User findById(String id);
	 public User update(User user);
}
