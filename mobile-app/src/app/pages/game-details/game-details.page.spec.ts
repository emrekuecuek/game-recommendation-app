import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { GameDetailsPage } from './game-details.page';

describe('GameDetailsPage', () => {
  let component: GameDetailsPage;
  let fixture: ComponentFixture<GameDetailsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GameDetailsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(GameDetailsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
