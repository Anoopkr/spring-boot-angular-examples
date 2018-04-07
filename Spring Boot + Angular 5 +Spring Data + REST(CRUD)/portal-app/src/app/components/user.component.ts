import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { User } from '../models/user.model';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-user',
  templateUrl: '../views/user.component.html',
  styles: []
})
export class UserComponent implements OnInit {

  users: User[];

  constructor(private router: Router, private userService: UserService) {

  }

  ngOnInit() {
    this.userService.getUsers()
      .subscribe( (data: User[]) => {
        this.users = data;
        
      });
          /*  this.userService.getUsers()
        .map((data: any) => data.json())
          .subscribe(
            (data: any) => {
                this.users = data;
            },
            err => console.log(err), // error
            () => console.log('getUserStatus Complete') // complete
          );*/
  };

  deleteUser(user: User): void {
    this.userService.deleteUser(user)
      .subscribe( data => {
        this.users = this.users.filter(u => u !== user);
      })
  };

}
