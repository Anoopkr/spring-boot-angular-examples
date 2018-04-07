package com.spring.example.userportal.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import com.spring.example.userportal.model.User;

@Repository
public interface UserRepository extends MongoRepository<User, Serializable>{

    void delete(User user);

    List<User> findAll();

    User findById(String id);

    User save(User user);
}
