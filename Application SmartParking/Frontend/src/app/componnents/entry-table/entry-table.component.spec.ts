import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntryTableComponent } from './entry-table.component';

describe('EntryTableComponent', () => {
  let component: EntryTableComponent;
  let fixture: ComponentFixture<EntryTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EntryTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EntryTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
